import logging
from typing import List, Dict


class KindleNoteProcessor:
    """Process the .txt file and create new notes."""

    def __init__(self, parsed_txt: list = []):
        self.notes: list = []
        self.parsed_txt = parsed_txt

        fmt="[%(levelname)s] %(asctime)s - %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=fmt)

    @property
    def parsed_txt(self) -> List[Dict[str, str]]:
        return self._parsed_txt

    @parsed_txt.setter
    def parsed_txt(self, text: List[Dict[str, str]]):
        if not isinstance(text, list):
            raise ValueError("Cannot process empty obj. str")
        self._parsed_txt = text

    def create_note(self, attrs: dict):
        self.notes.append(
            KindleNote(
                title=attrs.get("title"),
                author=attrs.get("author"),
                loc=attrs.get("location"),
                desc=attrs.get("description"),
                date=attrs.get("date"),
            )
        )

    def create_all_notes(self) -> None:
        for note in self._parsed_txt:
            if len(note.keys()) == 5:
                logging.info(f"Note added {note['title']}..")
                self.create_note(note)


class TxtParser:
    """Parse the data from the given .txt file."""

    def __init__(self, text, separator = ""):
        self.text = text
        self.separator = separator

    @property
    def separator(self) -> str:
        return self._separator

    @separator.setter
    def separator(self, sep: str):
        if not isinstance(sep, str):
            raise ValueError("Separator attribute has to be type 'str'.")
        self._separator = sep

    def split_text_into_lines(self) -> list:
        """Split .txt file into individual parsed notes."""
        return [
            self.process_note_content(note.splitlines())
            for note in self.text.split(self.separator)
            if note
        ]

    @staticmethod
    def process_note_content(note: List[str]) -> Dict[str, str]:
        """Try to select attributes title, date and description."""
        try:
            title_line: str = note[0]
            location_line: str = note[1]
            description: str = note[3]

        except IndexError:
            results: dict = {}
        else:
            title, author = title_line.split(" (", maxsplit=1)
            location, date = location_line.split("|", maxsplit=1)
            results: dict = {
                "date": date,
                "title": title,
                "location": location,
                "description": description,
                "author": author.rstrip(")"),
            }
        finally:
            return results


class KindleNote:
    """Create a note with proper attributes."""

    def __init__(self, title: str, loc: str, desc: str, date: str, author: str):
        self.desc = desc
        self.date = date
        self.title = title
        self.location = loc
        self.author = author

    def __repr__(self) -> str:
        return str(self.title)


if __name__ == "__main__":
    text = """
    ==========
    Faktomluva (Hans Rosling;Ola Rosling;Anna Roslingová Rönnlundová)
    - Your Highlight on Location 2724-2728 | Added on Wednesday, July 24, 2019 8:41:27 AM

    Největším orgánem našeho těla je kůže. Před objevem moderních léků patřila k nejhorším kožním nemocem syfilis. Začínala jako svědivé vřídky a pak si prokousala cestu do kostí, až postihla celou kostru. Nemoc způsobující ohavný vzhled a nesnesitelnou bolest měla v různých zemích různá jména. V Rusku chorobě říkali „polská nemoc“. V Polsku to byla „německá nemoc“, v Německu „francouzská nemoc“ a ve Francii „italská nemoc“. Italové vinu házeli zpátky a nazývali ji „francouzská nemoc“.
    ==========
    Life Is What You Make It (Peter Buffett)
    - Your Highlight on Location 233-234 | Added on Monday, August 19, 2019 2:07:48 PM

    The problem with honoring the rewards of work rather than the work itself is that the rewards can always be taken away.
    ==========
    Elon Musk (Ashlee Vance)
    - Your Highlight on page 127 | location 1943-1944 | Added on Thursday, 31 May 2018 19:38:29

    v oblasti rovníku, kde se planeta otáčí rychleji a pomáhá raketám v letu.
    ==========
    Linux Pocket Guide, 3E (Daniel J. Barrett)
    - Your Highlight on Location 2310-2314 | Added on Monday, February 18, 2019 10:09:26 AM

    Viewing Processes ps List process. uptime View the system load. w List active processes for all users. top Monitor resource-intensive processes interactively. free Display free memory.
    ==========
    Introducing Python (Bill Lubanovic)
    - Your Highlight on Location 6170-6171 | Added on Wednesday, June 26, 2019 10:18:02 AM

    Do not set debug = True in production web servers. It exposes too much information about your server to potential intruders.
    ==========
    """

    # rozděl zadaný text pomocí definovaného oddělovače
    txt = TxtParser(text)
    txt.separator = "==========\n"

    # zpracuj rozdělený text na jednotlivé atributy
    app = KindleNoteProcessor()
    app.parsed_txt = txt.split_text_into_lines()

    # zapiš všechny poznámky
    app.create_all_notes()

