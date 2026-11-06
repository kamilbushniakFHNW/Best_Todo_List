from datetime import date
from fpdf import FPDF
from view_task.view_task import count_done_subtasks


def export_pdf(tasks):
    if len(tasks) == 0:
        print("\nYou have no tasks to export.")
        return

    today = date.today()
    file_name = f"todo_{today.strftime('%d-%m-%Y')}.pdf"

    lines = ["To-Do List Report", f"Export date: {today.strftime('%d.%m.%Y')}", ""]
    for i in range(len(tasks)):
        task = tasks[i]
        lines.append(f"{i + 1}. {task['title']}")
        lines.append(f"    Due date: {task['due_date']} | Priority: {task['priority']} | Status: {task['status']}")

        subtasks = task["subtasks"]
        if len(subtasks) > 0:
            lines.append(f"    Subtasks: {count_done_subtasks(subtasks)}/{len(subtasks)} done")
            for j in range(len(subtasks)):
                lines.append(f"        {j + 1}. {subtasks[j]['title']} ({subtasks[j]['status']})")
        lines.append("")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    for line in lines:
        text = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")

    try:
        pdf.output(file_name)
    except OSError:
        print("Export failed: the file could not be saved.")
        return

    print(f"Report saved as {file_name}")