import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""
#     prompt = '(oo)'
#     def do_greet(self, line):
#         print ("hello")
    
#     def do_EOF(self, line):
#         return True

# if __name__ == '__main__':
#     HelloWorld().cmdloop()


# import cmd

# class HelloWorld(cmd.Cmd):
#     """Simple command processor example."""
    
#     def do_greet(self, person):
#         """greet [person]
#         Greet the named person"""
#         if person:
#             print ("hi,", person)
#         else:
#             print ('hi')
    
#     def do_EOF(self, line):
#         return True
    
#     def postloop(self):
#         print

# if __name__ == '__main__':
#     HelloWorld().cmdloop()

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    prompt = 'watin you want: '
    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print (greeting)
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()