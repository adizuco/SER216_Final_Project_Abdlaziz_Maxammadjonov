"""Generate workflow_diagram.png for the Digital Parking Permit System."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

fig, ax = plt.subplots(figsize=(11, 14))
ax.set_xlim(0, 11)
ax.set_ylim(0, 14)
ax.axis("off")

PROCESS = "#4A90E2"
DECISION = "#F5A623"
TERMINAL = "#7ED321"
END_C = "#D0021B"
VIOL = "#9B59B6"
TEXT = "white"


def box(cx, cy, w, h, label, color=PROCESS):
    p = FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        linewidth=1.5, edgecolor="black", facecolor=color,
    )
    ax.add_patch(p)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=11, color=TEXT, fontweight="bold")


def diamond(cx, cy, w, h, label, color=DECISION):
    pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    p = Polygon(pts, closed=True, linewidth=1.5, edgecolor="black", facecolor=color)
    ax.add_patch(p)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=10, color=TEXT, fontweight="bold")


def oval(cx, cy, w, h, label, color=TERMINAL):
    p = FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.5",
        linewidth=1.5, edgecolor="black", facecolor=color,
    )
    ax.add_patch(p)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=11, color=TEXT, fontweight="bold")


def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->", mutation_scale=18,
        linewidth=1.6, color="black",
    )
    ax.add_patch(a)


def label(x, y, text):
    ax.text(x, y, text, ha="center", va="center", fontsize=10,
            color="black", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor="#888"))


# Title
ax.text(5.5, 13.4, "Digital Parking Permit System — Workflow",
        ha="center", fontsize=16, fontweight="bold")

# Vertical column down the middle (x=5.5)
CX = 5.5

# 1 Start
oval(CX, 12.6, 1.6, 0.7, "Start", TERMINAL)
# 2 Vehicle Registration
box(CX, 11.4, 2.6, 0.9, "Vehicle Registration")
# 3 Permit Request
box(CX, 10.1, 2.6, 0.9, "Permit Request")
# 4 Zone Check
diamond(CX, 8.6, 3.0, 1.4, "Zone Check\nSpaces available?", DECISION)
# 5 Permit Approval
diamond(CX, 6.7, 3.2, 1.4, "Permit Approval?", DECISION)
# 6 Issue Permit
box(CX, 5.2, 2.8, 0.9, "Issue Permit\n+ QR Code")
# 7 Parking Verification
box(CX, 3.9, 2.8, 0.9, "Parking Verification")
# 8 Permit Valid?
diamond(CX, 2.5, 2.8, 1.3, "Permit Valid?", DECISION)

# Outcomes
oval(2.0, 0.8, 1.7, 0.7, "Allow Parking", TERMINAL)
box(8.6, 1.2, 2.0, 0.9, "Record\nViolation", VIOL)

# Rejected (right side)
box(9.5, 6.7, 2.0, 0.9, "Notify User\n(Rejected)", VIOL)

# End (very bottom center)
oval(CX, 0.4, 1.6, 0.6, "End", END_C)

# Arrows down the spine
arrow(CX, 12.25, CX, 11.85)
arrow(CX, 10.95, CX, 10.55)
arrow(CX, 9.65, CX, 9.3)
arrow(CX, 7.9, CX, 7.4)
arrow(CX, 6.0, CX, 5.65)
arrow(CX, 4.75, CX, 4.35)
arrow(CX, 3.45, CX, 3.15)

# Label for Yes on Approval and Zone
label(CX + 0.25, 7.95, "Yes")
label(CX + 0.25, 6.25, "Yes")

# Zone Check No -> back up to Permit Request (loop on left)
arrow(CX - 1.5, 8.6, 2.6, 8.6)
arrow(2.6, 8.6, 2.6, 10.1)
arrow(2.6, 10.1, 4.2, 10.1)
label(2.6, 9.35, "No\n(retry)")

# Permit Approval No -> Notify User (right)
arrow(CX + 1.6, 6.7, 8.5, 6.7)
label(7.6, 6.95, "No")

# Notify User -> End (right side, all the way down)
arrow(9.5, 6.25, 9.5, 0.4)
arrow(9.5, 0.4, CX + 0.8, 0.4)

# Permit Valid Yes -> Allow Parking
arrow(CX - 1.4, 2.5, 3.0, 2.5)
arrow(3.0, 2.5, 2.0, 1.15)
label(3.6, 2.7, "Yes")

# Permit Valid No -> Record Violation
arrow(CX + 1.4, 2.5, 8.0, 2.5)
arrow(8.0, 2.5, 8.6, 1.65)
label(7.4, 2.7, "No")

# Allow Parking -> End
arrow(2.0, 0.45, CX - 0.8, 0.4)

# Record Violation -> End
arrow(8.6, 0.75, CX + 0.8, 0.4)

plt.tight_layout()
plt.savefig("/Users/shahzod/abdulazizfinal/diagrams/workflow_diagram.png",
            dpi=180, bbox_inches="tight", facecolor="white")
print("Saved workflow_diagram.png")
