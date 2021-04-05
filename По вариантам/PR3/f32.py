class C32:
    state = 'A'

    def file(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'B'
            return 5
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise RuntimeError

    def unite(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise RuntimeError

    def throw(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        else:
            raise RuntimeError

    def slog(self):
        if self.state == 'E':
            self.state = 'A'
            return 7
        elif self.state == 'G':
            self.state = 'E'
            return 10
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'H':
            self.state = 'F'
            return 11
        else:
            raise RuntimeError


# print("First case: ")
# a = C32()
# print(f"o.file = {a.file()}")
# print(f"o.unite = {a.unite()}")
# print(f"o.throw = {a.throw()}")
# print(f"o.file = {a.file()}")
# print(f"o.unite = {a.unite()}")
# print(f"o.unite = {a.unite()}")
# print(f"o.throw = {a.throw()}")
# print(f"o.unite = {a.unite()}")
# print(f"o.unite = {a.unite()}")
# print(f"o.slog = {a.slog()}")
# print(f"o.file = {a.file()}")
# print(f"o.slog = {a.slog()}")
# print(f"o.slog = {a.slog()}")
# print(f"o.slog = {a.slog()}")
# print(f"o.slog = {a.slog()}")
#
# print("\nSecond case:")
# b = C32()
# print(f"o.file = {b.file()}")
# print(f"o.unite = {b.unite()}")
# print(f"o.throw = {b.throw()}")
# print(f"o.file = {b.file()}")
# print(f"o.unite = {b.unite()}")
# print(f"o.unite = {b.unite()}")
# print(f"o.throw = {b.throw()}")
# print(f"o.unite = {b.unite()}")
# print(f"o.unite = {b.unite()}")
# print(f"o.slog = {b.slog()}")
# print(f"o.file = {b.file()}")
# print(f"o.slog = {b.slog()}")
# print(f"o.slog = {b.slog()}")
# print(f"o.slog = {b.slog()}")
# print(f"o.file = {b.file()}")
# print(f"o.slog = {b.slog()}")
# print(f"o.file = {b.file()}")
