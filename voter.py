import sys
import argparse


commands = ['register', 'verify voters', 'vote', 'verify my vote',
            'verify all votes', 'count votes']

def main(argv):

    args = sys.argv.pop()
    command_string = ' '.join(sys.argv[2:])
    if command_string in commands:
        print 'id: ', sys.argv[1], 'command: ', command_string, 'args: ', args
    else:
        print "Unknown command. Please enter the valid command."

if __name__ == "__main__":
    main(sys.argv[1:])

#parser = argparse.ArgumentParser()
#parser.add_argument('--arguments')
#args = parser.parse_args()
#print 'arguments: {}'.format(args.arguments)
