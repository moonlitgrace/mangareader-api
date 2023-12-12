from typing import Dict

selectors_dict: Dict = {
    "title": ".anis-content h2.manga-name",
    "alt_title": ".anis-content div.manga-name-or",
    "type": ".anis-content .anisc-info .item:nth-child(1) a",
    "genres": ".anis-content .genres a",
    "status": ".anis-content .anisc-info .item:nth-child(2) .name",
    "score": ".anis-content .anisc-info .item:nth-child(6) .name",
    "cover_src": ".anis-content .manga-poster-img",
    "synopsis": ".description-modal",
}
