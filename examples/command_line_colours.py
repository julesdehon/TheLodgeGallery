import zmq


def fill_colour(colour):
    return {
        "action": "fill_colour",
        "fill_colour": {
            "colour": colour
        }
    }


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        colour = input("Colour to send:\n> ")
        socket.send_json(fill_colour(colour))
        response = socket.recv_json()
        print("Received response: {}".format(response))


if __name__ == "__main__":
    main()
