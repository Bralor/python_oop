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
    Faktomluva (Hans Rosling;Ola Rosling;Anna Roslingov?? R??nnlundov??)
    - Your Highlight on Location 2724-2728 | Added on Wednesday, July 24, 2019 8:41:27 AM

    Nejv??t????m org??nem na??eho t??la je k????e. P??ed objevem modern??ch l??k?? pat??ila k nejhor????m ko??n??m nemocem syfilis. Za????nala jako sv??div?? v????dky a pak si prokousala cestu do kost??, a?? postihla celou kostru. Nemoc zp??sobuj??c?? ohavn?? vzhled a nesnesitelnou bolest m??la v r??zn??ch zem??ch r??zn?? jm??na. V Rusku chorob?? ????kali ???polsk?? nemoc???. V Polsku to byla ???n??meck?? nemoc???, v N??mecku ???francouzsk?? nemoc??? a ve Francii ???italsk?? nemoc???. Italov?? vinu h??zeli zp??tky a naz??vali ji ???francouzsk?? nemoc???.
    ==========
    Life Is What You Make It (Peter Buffett)
    - Your Highlight on Location 233-234 | Added on Monday, August 19, 2019 2:07:48 PM

    The problem with honoring the rewards of work rather than the work itself is that the rewards can always be taken away.
    ==========
    Elon Musk (Ashlee Vance)
    - Your Highlight on page 127 | location 1943-1944 | Added on Thursday, 31 May 2018 19:38:29

    v oblasti rovn??ku, kde se planeta ot?????? rychleji a pom??h?? raket??m v letu.
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

    # rozd??l zadan?? text pomoc?? definovan??ho odd??lova??e
    txt = TxtParser(text)
    txt.separator = "==========\n"

    # zpracuj rozd??len?? text na jednotliv?? atributy
    app = KindleNoteProcessor()
    app.parsed_txt = txt.split_text_into_lines()

    # zapi?? v??echny pozn??mky
    app.create_all_notes()

