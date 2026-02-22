import numpy as np
import matplotlib
import io

def map(place_coords, city_limits, water, streets):
    rand_num = np.random.rand(2)
    while np.sqrt(rand_num[0]**2 + rand_num[1]**2) > 1:
        # print('trying again')
        rand_num = rand_num = np.random.rand(2)
    rand_num[0] = (rand_num[0] - 0.5) / 54.6 / 2
    rand_num[1] = (rand_num[1] - 0.5) / 69 / 2
    area_center = place_coords - rand_num
    ax = city_limits.plot(color="tan", alpha= 0.6)
    water.plot(color="lightblue", ax=ax)
    streets.plot(color="gray", ax=ax, alpha=1)
    ax.set_axis_off()
    # ax.plot(place_coords[0], place_coords[1], marker='o', alpha=0.5)
    ax.add_patch(matplotlib.patches.Ellipse((area_center[0], area_center[1]), width = 0.6 / 52, height = 0.6 / 69,
                            edgecolor='red', facecolor='salmon', linewidth=0.5))
    ax.set_xlim(area_center[0] - 0.025,
                area_center[0] + 0.025)
    ax.set_ylim(area_center[1] - 0.02,
                area_center[1] + 0.02)

    try:
        f = io.StringIO()
        matplotlib.pyplot.savefig(f, format="svg", bbox_inches='tight')  
        print("SVG file saved successfully as f")
    except Exception as e:
        print(f"Error saving SVG: {e}")

    matplotlib.pyplot.close()
    return f