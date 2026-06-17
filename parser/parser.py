class Parser:
    def __init__(self, filename):
        self.lines = []
        self.index = 0
        self.current_instruction = None

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.split("//")[0].strip()

                if line:
                    self.lines.append(line)

    def has_more_instructions(self):
        return self.index < len(self.lines)

    def advance(self):
        if self.has_more_instructions():
            self.current_instruction = self.lines[self.index]
            self.index += 1
            return self.current_instruction

        return None

    def instruction_type(self):
        if self.current_instruction is None:
            return None

        if self.current_instruction.startswith("@"):
            return "A_INSTRUCTION"

        if (
            self.current_instruction.startswith("(")
            and self.current_instruction.endswith(")")
        ):
            return "LABEL"

        return "C_INSTRUCTION"

    def symbol(self):
        if self.instruction_type() == "A_INSTRUCTION":
            return self.current_instruction[1:]

        if self.instruction_type() == "LABEL":
            return self.current_instruction[1:-1]

        return None

    def dest(self):
        if self.instruction_type() != "C_INSTRUCTION":
            return None

        if "=" in self.current_instruction:
            return self.current_instruction.split("=")[0]

        return None

    def comp(self):
        if self.instruction_type() != "C_INSTRUCTION":
            return None

        instruction = self.current_instruction

        if "=" in instruction:
            instruction = instruction.split("=")[1]

        if ";" in instruction:
            instruction = instruction.split(";")[0]

        return instruction

    def jump(self):
        if self.instruction_type() != "C_INSTRUCTION":
            return None

        if ";" in self.current_instruction:
            return self.current_instruction.split(";")[1]

        return None