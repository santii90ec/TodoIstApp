resource "aws_dynamodb_table" "sapp_dynamo_table" {
  name = var.dynamo_table_name
  hash_key  = "ID"

  attribute {
    name = "ID"
    type = "S"
  }

  billing_mode = "PAY_PER_REQUEST"
}
