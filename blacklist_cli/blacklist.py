from typing import List


class Blacklist:
    def __init__(self, file):
        self.file = file
        self.BEGIN = "# Blacklisted URLs - BEGIN\n"
        self.END = "# Blacklisted URLs - END\n"
        self.REDIRECT_IP = "127.0.0.1"

    def set_domains(self, domains):
        with open(self.file, "r") as f:
            lines = f.readlines()

        begin_index = lines.index(self.BEGIN) if self.BEGIN in lines else len(lines)

        with open(self.file, "w") as f:
            # Write original host file until blacklist_cli section
            for line in lines[:begin_index]:
                f.write(line)

            # Write blacklist_cli section
            f.write(self.BEGIN)

            for domain in domains:
                f.write(f"127.0.0.1 {domain}\n")
                f.write(f"::1 {domain}\n")

            f.write(self.END)

            # Write rest of original host file
            if self.END in lines:
                end_index = lines.index(self.END)

                for line in lines[end_index + 1:]:
                    f.write(line)

    def get_domains(self) -> List[str]:
        with open(self.file, "r") as f:
            lines = f.readlines()

            if self.BEGIN in lines and self.END in lines:
                start = lines.index(self.BEGIN) + 1
                end = lines.index(self.END)
                lines = lines[start:end]
                return list(set([lines.split()[1].strip() for lines in lines]))
            else:
                return []
