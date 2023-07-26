class Sim:
    __globals = {
        # Global
        "WIDTH": 1760,
        "HEIGHT": 990,

        # Colors
        "colors": {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GREEN": (0, 255, 0),
            "DARK_GREEN": (0, 155, 0),
            "BLUE": (0, 0, 100),
            "DARK_BLUE": (0, 0, 100),
            "CYAN": (0, 255, 255)
        },

        # Ant
        "ant": {
            "SIZE": 2,
            "SPEED": 2,
            "AMOUNT": 500,
        },

        # Nest
        "nest": {
            "RADIUS": 20,
        },

        # Food
        "food": {
            "RADIUS": 45,
            "AMOUNT": 15,
        },
        
        # Trail
        "trail": {
            "DECAY_RATE": 20,
        },  

        # Rendering
        "render": {
            "UPDATE_TIME": 250,     # 0 - 1000
            "DRAW_TIME": 0,
        },
	}

    @staticmethod
    def conf(name, sub=None):
        if sub:
            return Sim.__globals[name][sub]
        else:
            return Sim.__globals[name]