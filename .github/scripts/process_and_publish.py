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

def process_yaml_file(yaml_file):
    """
    Processes the specified YAML file, cloning repos and copying specified
    chart paths to the charts directory with a unique directory for each chart.
    """
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    for repo in data.get('repos', []):
        repo_url = repo['url']
        paths = repo['paths']

        # Extract the repository name from the URL
        repo_name = repo_url.split('/')[-1]

        for path in paths:
            # Extract the chart name from the path
            chart_name = path.split('/')[-1]
            
            # Construct a unique directory name for each chart
            unique_dir_name = f"{repo_name}_{chart_name}"
            clone_target_dir = os.path.join('cloned_repos', unique_dir_name)

            print(f"Processing {unique_dir_name} in {clone_target_dir}...")

            # Check if the repo has already been cloned into this unique directory
            if not os.path.exists(clone_target_dir):
                # Clone the repository into the target directory
                print(f"Cloning {repo_url} into {clone_target_dir}")
                Repo.clone_from(repo_url, clone_target_dir, multi_options=['--depth', '1'])
            else:
                print(f"Directory {clone_target_dir} exists, assuming repository already cloned.")

            # Adjust the source directory based on the cloned repo structure
            # Since we're cloning the entire repo for each chart, adjust the chart_path accordingly
            adjusted_chart_path = os.path.join(clone_target_dir, path)

            # Now, copy the chart to the charts directory
            copy_chart_to_charts_dir(adjusted_chart_path, path, chart_name)

def copy_chart_to_charts_dir(source_dir, chart_path, chart_name):
    """
    Adjusted to handle unique cloned directories for each chart.
    Copies the chart from the specified path within the cloned repo to the
    charts directory, creating a subdirectory named after the chart.
    """
    dest_path = os.path.join(charts_dir, chart_name)

    # Calculate the full source path - now directly using source_dir since it's uniquely cloned
    full_source_path = source_dir

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    shutil.copytree(full_source_path, dest_path)

    print(f"Copied {full_source_path} to {dest_path}")


if __name__ == "__main__":
    # Ensure the charts directory exists
    os.makedirs(charts_dir, exist_ok=True)
    # Process the YAML configuration
    process_yaml_file(yaml_file)
