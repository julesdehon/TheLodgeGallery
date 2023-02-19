import fastjsonschema
from colour import Color


class MessageHandler:
  def __init__(self, matrix, matrix_action_schema):
    self.matrix = matrix
    self.validate = fastjsonschema.compile(matrix_action_schema)
    self.action = {
      "fill_colour": self.handle_fill_colour,
    }

  def handle_message(self, message):
    try:
      self.validate(message)
    except fastjsonschema.JsonSchemaException as e:
      return self.error_response(e.message)
    
    action = message["action"]
    return self.action[action](message[action])
  
  def handle_fill_colour(self, fill_colour_msg):
    try:
      colour = Color(fill_colour_msg["colour"])
    except Exception as e:
      return self.error_response(
        "Unable to convert colour {}. Reason: {}"
        .format(fill_colour_msg["colour"], str(e))
      )
    
    r, g, b = [val * 255 for val in colour.get_rgb()]
    print("Filling matrix with {} {} {}".format(r, g, b))
    self.matrix.Fill(r, g, b)

    return {
      "response": "ok"
    }
  
  def error_response(self, reason):
    return {
      "response": "error",
      "error": {
        "reason": "Invalid request. {}".format(reason)
      }
    }