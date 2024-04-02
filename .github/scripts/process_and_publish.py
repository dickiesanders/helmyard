import os
import shutil
import yaml
from git import Repo

yaml_file = './repos.yaml'

# Target directory for the charts
charts_dir = './charts/'

def clone_repo(repo_url, target_dir):
    """
    Clones the specified repo URL into the target directory. If the directory
    already exists, it assumes the repository is already cloned and skips the operation.
    """
    if not os.path.exists(target_dir):
        print(f"Cloning {repo_url} into {target_dir}")
        Repo.clone_from(repo_url, target_dir)
    else:
        print(f"Directory {target_dir} exists, assuming repository already cloned.")

# def copy_chart_to_charts_dir(source_dir, chart_path):
#     """
#     Copies the chart from the specified path within the cloned repo to the
#     charts directory, creating a subdirectory named after the last segment of the path.
#     """
#     chart_name = chart_path.split('/')[-1]
#     dest_path = os.path.join(charts_dir, chart_name)

#     # Calculate the full source path
#     full_source_path = os.path.join(source_dir, chart_path)

#     if os.path.exists(dest_path):
#         shutil.rmtree(dest_path)
#     shutil.copytree(full_source_path, dest_path)

#     print(f"Copied {full_source_path} to {dest_path}")

def copy_chart_to_charts_dir(source_dir, chart_path):
    """
    Copies the chart from the specified path within the cloned repo to the
    charts directory, creating a subdirectory named after the last segment of the path.
    """
    chart_name = chart_path.split('/')[-1]
    print(chart_name)
    dest_path = os.path.join(charts_dir, chart_name)

    # Calculate the full source path
    full_source_path = os.path.join(source_dir, chart_path)

    if not os.path.exists(full_source_path):
        print(f"Source path does not exist: {full_source_path}")
        return

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    shutil.copytree(full_source_path, dest_path)

    print(f"Copied {full_source_path} to {dest_path}")

def process_yaml_file(yaml_file):
    """
    Processes the specified YAML file, cloning repos and copying specified
    chart paths to the charts directory.
    """
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    for repo in data.get('repos', []):
        repo_url = repo['url']
        paths = repo['paths']

        # Create a directory name based on the repo URL to clone the repo
        repo_dir_name = repo_url.split('/')[-1]  # Use the repo name as the directory
        clone_target_dir = os.path.join('cloned_repos', repo_dir_name)

        # Clone the repository into the target directory
        clone_repo(repo_url, clone_target_dir)

        # Copy each specified path to the charts directory
        for path in paths:
            copy_chart_to_charts_dir(clone_target_dir, path)

if __name__ == "__main__":
    # Ensure the charts directory exists
    os.makedirs(charts_dir, exist_ok=True)
    # Process the YAML configuration
    process_yaml_file(yaml_file)
