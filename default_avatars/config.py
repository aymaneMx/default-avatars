import re

COLORS = [
    ['#DF7FD7', '#DF7FD7', '#591854'],
    ['#E3CAC8', '#DF8A82', '#5E3A37'],
    ['#E6845E', '#E05118', '#61230B'],
    ['#E0B050', '#E6CB97', '#614C23'],
    ['#9878AD', '#492661', '#C59BE0'],
    ['#787BAD', '#141961', '#9B9FE0'],
    ['#78A2AD', '#104F61', '#9BD1E0'],
    ['#78AD8A', '#0A6129', '#9BE0B3'],
]

INITIALS_SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" pointer-events="none" width="200" height="200">
  <defs>
    <linearGradient id="grad">
    <stop offset="0%" stop-color="{color1}" />
    <stop offset="100%" stop-color="{color2}" />
    </linearGradient>
  </defs>
  <rect width="200" height="200" rx="0" ry="0" fill="url(#grad)"></rect>
  <text text-anchor="middle" y="50%" x="50%" dy="0.35em"
        pointer-events="auto" fill="{text_color}" font-family="sans-serif"
        style="font-weight: 400; font-size: 80px">{text}</text>
</svg>
""".strip()
INITIALS_SVG_TEMPLATE = re.sub('(\s+|\n)', ' ', INITIALS_SVG_TEMPLATE)

LOGO_SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" width="400px" height="400px" viewBox="0 0 400 400">
    <rect class="cls-1" width="400" height="400" fill="{color1}" />
    <g width="400px" height="400px">
        <path 
            fill="{logo_color}" 
            d="M153.62,301.59c94.34,0,145.94-78.16,145.94-145.94,0-2.22,0-4.43-.15-6.63A104.36,104.36,0,0,0,325,
            122.47a102.38,102.38,0,0,1-29.46,8.07,51.47,51.47,0,0,0,22.55-28.37,102.79,102.79,0,0,1-32.57,12.45,
            51.34,51.34,0,0,0-87.41,46.78A145.62,145.62,0,0,1,92.4,107.81a51.33,51.33,0,0,0,15.88,68.47A50.91,50.91,
            0,0,1,85,169.86c0,.21,0,.43,0,.65a51.31,51.31,0,0,0,41.15,50.28,51.21,51.21,0,0,1-23.16.88,51.35,51.35,
            0,0,0,47.92,35.62,102.92,102.92,0,0,1-63.7,22A104.41,104.41,0,0,1,75,278.55a145.21,145.21,0,0,0,78.62,23"
        />
    </g>

</svg>
""".strip()
LOGO_SVG_TEMPLATE = re.sub('(\s+|\n)', ' ', LOGO_SVG_TEMPLATE)
