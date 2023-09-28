variable "project_id" {
  type    = string
  default = "ASX-Code-Challenge"
}

variable "instances" {
  type = map(object({
    machine_type = string
    zone         = string
    description  = string
  }))
  default = {
    instance1 = {
      description  = "Description for instance1"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    },
    instance2 = {
      description  = "Description for instance2"
      machine_type = "n1-standard-2"
      zone         = "us-central1-b"
    }
  }

}

variable "service_account" {
  type    = string
  default = ""
}

variable "scopes" {
  type    = list(string)
  default = []
}
