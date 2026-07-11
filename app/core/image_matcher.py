import re
from difflib import SequenceMatcher


class ImageMatcher:

    @staticmethod
    def normalize(text):

        text = text.lower()

        # Remove file extension
        text = re.sub(r"\.[a-z0-9]+$", "", text)

        # Replace separators with spaces
        text = text.replace("_", " ")
        text = text.replace("-", " ")

        # Remove extra spaces
        text = " ".join(text.split())

        return text

    @staticmethod
    def find_best_match(menu_name, image_names):

        menu_name = ImageMatcher.normalize(menu_name)

        best_name = ""
        best_score = 0

        for image in image_names:

            image_name = ImageMatcher.normalize(image)

            score = SequenceMatcher(
                None,
                menu_name,
                image_name,
            ).ratio()

            # Bonus for substring matches
            if menu_name in image_name or image_name in menu_name:
                score += 0.25

            if score > best_score:
                best_score = score
                best_name = image

        print(
            f"Best Match: {best_name} | Score: {best_score:.2f}"
        )

        if best_score >= 0.60:
            return best_name

        return ""