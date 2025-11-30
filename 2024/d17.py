from timeit import default_timer as timer
import re

#Program:
# 2,4: bst : B <- A % 8     : B in 0 thru 7
# 1,6: bxl : B <- B ^ 110   : B in 0 thru 7
# 7,5: cdv : C <- A // 2**B : C = A // (1 thru 128) so just increment C?
# 4,4: bxc : B <- B ^ C     : in same range as C now.  (nearest C?)
# 1,7: bxl : B <- B ^ 111   : in same range as C still (nearest 7?)
# 0,3: adv : A <- A // 2**3 : A // 8
# 5,5: out : B % 8          : output.append(B % 8)
# 3,0: jnz : end if A == 0 else goto 0

class Debugger:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ip = 0
        self.output_data = []

    def get_output(self):
        return ','.join( [str(x) for x in self.output_data] )

    def get_combo(self, combo: int):
        if combo == 1 or combo == 2 or combo == 3:
            return int(combo)
        elif combo == 4:
            return self.a
        elif combo == 5:
            return self.b
        elif combo == 6:
            return self.c
        else:
            raise ValueError("Invalid combo")

    def adv(self, combo: int):
        """
        The adv instruction (opcode 0) performs division.
        The numerator is the value in the A register.
        The denominator is found by raising 2 to the power of the instruction's combo operand.
        (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
         The result of the division operation is truncated to an integer and then written to the A register.
        """
        input = self.get_combo(combo)
        numerator = self.a
        denominator = 2**input
        self.a = numerator // denominator
        self.ip += 2

    def bxl(self, literal: int):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B
            and the instruction's literal operand, then stores the result in register B.
        """
        self.b = self.b ^ literal
        self.ip += 2

    def bst(self, combo: int):
        """
        The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
           (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        """
        input = self.get_combo(combo)
        self.b = input % 8
        self.ip += 2

    def jnz(self, literal: int):
        """
        The jnz instruction (opcode 3) does nothing if the A register is 0.
        However, if the A register is not zero, it jumps by setting the instruction pointer
        to the value of its literal operand;
        if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        """
        if self.a == 0:
            self.ip += 2
            return

        self.ip = literal
        pass

    def bxc(self, literal: int):
        """
        The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
        then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
        """
        self.b = self.b ^ self.c
        self.ip += 2

    def out(self, combo: int):
        """
        The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
            then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        """
        input = self.get_combo(combo)
        self.output_data.append(input % 8)
        self.ip += 2

    def bdv(self, combo: int):
        """
        The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        """
        input = self.get_combo(combo)
        numerator = self.a
        denominator = 2**input
        self.b = numerator // denominator
        self.ip += 2

    def cdv(self, combo: int):
        """
        The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
        """
        input = self.get_combo(combo)
        numerator = self.a
        denominator = 2**input
        self.c = numerator // denominator
        self.ip += 2

    def run(self, solution_2=False):
        opcode_to_func = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ]
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            func = opcode_to_func[opcode]
            func(operand)
            if solution_2 and len(self.output_data) > len(self.program):
                break

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = f.read().strip()
        register_pattern = r"Register\s+([A-C]):\s+(\d+)"

        registers = {}
        for match in re.finditer(register_pattern, data):
            register, value = match.groups()
            registers[register] = int(value)

        program_pattern = r"Program:\s*([\d,]+)"
        program_match = re.search(program_pattern, data)
        program_sequence = list(map(int, program_match.group(1).split(','))) if program_match else []

        debugger = Debugger(registers['A'], registers['B'], registers['C'], program_sequence)

    return debugger


def solution_1(db):
    db.run()
    return db.get_output()

def solution_2(puzzle_input):
    oct = []
    def backtrack(i):
        if i == 16:
            return True
        for j in range(8):
            oct.append(j)
            db = parse_input(puzzle_input)
            db.a = int(''.join([str(x) for x in oct]), 8)
            db.run()
            print(db.get_output())
            check = db.program[::-1][:i+1]
            if db.output_data[::-1] == check:
                if backtrack(i + 1):
                    return True
                print(db.get_output()[:i])
                print(int(''.join([str(x) for x in oct]), 8))
            oct.pop()
    backtrack(0)
    print(int(''.join([str(x) for x in oct]), 8))
    return int(''.join([str(x) for x in oct]), 8)

if __name__ == "__main__":
    # start = timer()
    # db = parse_input("puzzle_input//d17_input.txt")
    # result = solution_1(db)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

    # start = timer()
    # result = solution_2("puzzle_input//d17_input_ex2.txt")
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {result}')

    start = timer()
    result = solution_2("puzzle_input//d17_input.txt")
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result}')


