from screeninfo import get_monitors

monitors_list = get_monitors()
width = getattr(monitors_list[0],'width') 
height = getattr(monitors_list[0],'height') 
