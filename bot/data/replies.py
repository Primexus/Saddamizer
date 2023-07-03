import re

sleep_regex = re.compile(r'\bsleep\b', re.IGNORECASE)
sleep = (
    'IS THIS A SADDAM HUSSEIN REFERENCE?!',
    'Is this, by any chance, a reference to Saddam Hussein?',
    'Are you subtly referring to Saddam Hussein?',
    'Wait, is this about Saddam Hussein?',
    'Hold on, I sense a Saddam Hussein reference here!',
    'This seems suspiciously similar to Saddam Hussein...',
    'Ah, a potential allusion to Saddam Hussein!',
    'Could it be? A hidden connection to Saddam Hussein?',
    'I can\'t help but wonder, is this somehow related to Saddam Hussein?'
)

quoi_regex = re.compile(r'\bquoi\b', re.IGNORECASE)
quoi = (
    'feur',
    'feur?',
    'feur.',
    'feur!',
    'feur...',
    'feur?!',
    'feur?!?!',
    'feur?!?!?!',
    'feur HAHAHAHAHAH',
)

