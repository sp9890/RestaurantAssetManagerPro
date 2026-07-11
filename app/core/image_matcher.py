from difflib import SequenceMatcher


class ImageMatcher:

    @staticmethod
    def find_best_match(menu_name, image_names):

        menu_name = menu_name.lower()

        best_name = ""
        best_score = 0

        for image in image_names:

            score = SequenceMatcher(
                None,
                menu_name,
                image.lower()
            ).ratio()

            if score > best_score:
                best_score = score
                best_name = image

        if best_score >= 0.55:
            return best_name

        return ""