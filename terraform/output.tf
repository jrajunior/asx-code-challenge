output "vm_hostnames" {
  value = { for instance_key, instance_value in google_compute_instance.vm : instance_key => instance_value.hostname }
}

output "vm_ip_addresses" {
  value = { for instance_key, instance_value in google_compute_instance.vm : instance_value.hostname => google_compute_instance.vm[instance_key].network_interface[0].network_ip }
}
