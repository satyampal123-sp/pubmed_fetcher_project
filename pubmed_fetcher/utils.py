from typing import Optional

def is_non_academic(affiliation: Optional[str]) -> bool:
    if not affiliation:
        return False
    affiliation = affiliation.lower()
    academic_keywords = ['university', 'college', 'institute', 'hospital', 'school', 'department', 'center', 'centre']
    return not any(word in affiliation for word in academic_keywords)
