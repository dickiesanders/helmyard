# Helmyard

Helmyard automates the process of managing and publishing Helm charts by interpreting structured YAML configurations. Designed for Kubernetes administrators and developers, it simplifies the synchronization, organization, and deployment of Helm charts across multiple repositories.

## Features

- **YAML-Driven Workflow**: Define your Helm chart sources and destinations in a simple YAML file.
- **Automated Chart Management**: Automatically clones repositories, extracts Helm charts, and organizes them into a predefined structure.
- **Seamless Integration**: Easily integrates with CI/CD pipelines for streamlined chart publishing.

## Getting Started

### Prerequisites

- Python 3.6 or later.
- GitPython: `pip install gitpython`
- PyYAML: `pip install pyyaml`
- Access to Git repositories listed in your configuration YAML.

### Installation

1. Clone the Helmyard repository:
   ```bash
   git clone https://github.com/yourusername/helmyard.git
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Create a `repos.yaml` file in the root of the helmyard directory. Structure it as follows:
   ```yaml
   repos:
     - url: "https://github.com/example/repo1"
       paths:
         - "helm/chart1"
         - "helm/chart2"
     - url: "https://github.com/example/repo2"
       paths:
         - "helm/chart3"
   ```
   Replace the URLs and paths with the actual locations of your Helm charts.

### Usage

This process is managed by GitHub Actions:

Additions to the `repos.yaml` will trigger an action to build and publish the helm charts to `https://dickiesanders.github.io/helmyard`

helmyard will clone the specified repositories, extract the Helm charts based on the paths provided, and organize them into the `./charts/` directory, ready for deployment or further action.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

See `CONTRIBUTING.md` for detailed contribution guidelines.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- This project was inspired by the need for a streamlined approach to manage Helm charts across multiple Kubernetes deployments.
- Thanks to all contributors and users for their support and suggestions.

---

### Additional Notes:

- **Customize the Acknowledgments**: Tailor the acknowledgments section to thank specific individuals, projects, or resources that helped inspire or guide your project.
- **Add a `CONTRIBUTING.md`**: If you plan to welcome contributions, create a `CONTRIBUTING.md` file to detail how others can contribute to your project.
- **License**: Ensure the license type (`MIT` in this template) matches your project's license. Adjust the `LICENSE` reference accordingly.

This README template provides a foundation, but the success of your project's documentation depends on its accuracy, clarity, and completeness. Consider expanding sections with more detailed examples, screenshots, or workflows as your project evolves.