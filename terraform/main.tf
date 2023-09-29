resource "google_compute_instance" "vm" {
  for_each     = { for instance in var.instances : "${var.project_id}-instance-${index(var.instances, instance)}" => instance }
  project      = var.project_id
  name         = each.key
  description  = each.value.description
  machine_type = each.value.machine_type
  zone         = each.value.zone
  hostname     = "${each.key}-${each.value.zone}.asx.com.au"

  # Create Disk and Network Interface so it is possible to run "terraform validate"
  # - (Based on Terraform Docs: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#example-usage)
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
      }
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  # the code section "dynamic"  is looping the var "service_account" declarated in the input.tf file
  # if the "service_account" is not null/empty the dynamic will create 1 resource, if not (if empty/null) the resource will not be created
  # if the resource is to be created, its content will have:
  # - an email from the variable "service_account" in the input.tf
  # - a scope from the variable "scopes" in the input.tf

  # The use of dynamic has benefits itself as in creating resources dinamically and conditionally.
  # - When its operation is combined with for_each, it is enhanced by the use of a list of conditions, provides reduced amount of code and make it easier to maintain.

  dynamic "service_account" {
    for_each = var.service_account != "" ? [1] : []
    content {
      email  = var.service_account
      scopes = var.scopes
    }
  }
}