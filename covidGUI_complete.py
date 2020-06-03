# GUI for COVID-19 API 
import tkinter as tk
import requests

# Create initial GUI
window = tk.Tk()

window.title("COVID-19 Live Statistics")

window.geometry("600x800")

# World Summary Function
def summary_generator():

    url = "https://api.covid19api.com/summary"

    # Get response in terms of JSON of COVID-19 summary and saves Global
    response = requests.get(
        url,
        headers={
            "Accept": "application/json"}
    ).json()
    response = dict(response['Global'])

    return response

# World Summary Display Function
def summary_display():

    summary = summary_generator()
    summary_display = tk.Text(master=window, height=7, width=40)
    summary_display.grid(column=0, row=4)

    # Insert summary into text box
    summary_display.insert(
        tk.END, f"Number of new confirmed: {summary['NewConfirmed']}")
    summary_display.insert(tk.END, "\n")
    summary_display.insert(
        tk.END, f"Number of confirmed cases: {summary['TotalConfirmed']}")
    summary_display.insert(tk.END, "\n")
    summary_display.insert(
        tk.END, f"Number of new death(s): {summary['NewDeaths']}")
    summary_display.insert(tk.END, "\n")
    summary_display.insert(
        tk.END, f"Number of total death(s): {summary['TotalDeaths']}")
    summary_display.insert(tk.END, "\n")
    summary_display.insert(
        tk.END, f"Number of new recovered: {summary['NewRecovered']}")
    summary_display.insert(tk.END, "\n")
    summary_display.insert(
        tk.END, f"Number of total recovered: {summary['TotalRecovered']}")

# Country Summary Function
def country_generator():

    url_1 = "https://api.covid19api.com/summary"

    # Get response in terms of JSON of COVID-19 summary
    response_1 = requests.get(
        url_1,
        headers={
            "Accept": "application/json"}
    ).json()

    # Filters by queried country
    country = filter(lambda val: val['Country']
                     == entry.get(), response_1["Countries"])
    country = list(country)
    return country

# Country Summary Display Function
def country_display():

    country_show = country_generator()
    country_display = tk.Text(master=window, height=7, width=40)
    country_display.grid(column=0, row=9)

    # Insert country statistics into GUI
    country_display.insert(
        tk.END, f"Number of new confirmed: {country_show[0]['NewConfirmed']}")
    country_display.insert(tk.END, "\n")
    country_display.insert(
        tk.END, f"Number of confirmed cases: {country_show[0]['TotalConfirmed']}")
    country_display.insert(tk.END, "\n")
    country_display.insert(
        tk.END, f"Number of new death(s): {country_show[0]['NewDeaths']}")
    country_display.insert(tk.END, "\n")
    country_display.insert(
        tk.END, f"Number of total death(s): {country_show[0]['TotalDeaths']}")
    country_display.insert(tk.END, "\n")
    country_display.insert(
        tk.END, f"Number of new recovered: {country_show[0]['NewRecovered']}")
    country_display.insert(tk.END, "\n")
    country_display.insert(
        tk.END, f"Number of total recovered: {country_show[0]['TotalRecovered']}")

# Country Percentage Comparison Function
def percent_generator():

    url_2 = "https://api.covid19api.com/summary"

    # Get response in terms of JSON of COVID-19 summary
    response_2 = requests.get(
        url_2,
        headers={
            "Accept": "application/json"}
    ).json()

    return response_2

# Country Percentage Comparison Display Function
def percent_display():

    full_stats = percent_generator()

    stats_display = tk.Text(master=window, height=7, width=45)
    stats_display.grid(column=0, row=14)

    # Filters by queried country
    comp_country = filter(
        lambda val: val['Country'] == entry2.get(), full_stats["Countries"])
    comp_country = list(comp_country)

    # Save comparison variables
    per_new_case = round(
        comp_country[0]['NewConfirmed']/full_stats['Global']['NewConfirmed'] * 100, 1)
    total_con_case = round(
        comp_country[0]['TotalConfirmed']/full_stats['Global']['TotalConfirmed'] * 100, 1)
    new_deaths = round(
        comp_country[0]['NewDeaths']/full_stats['Global']['NewDeaths'] * 100, 1)
    total_deaths = round(
        comp_country[0]['TotalDeaths']/full_stats['Global']['TotalDeaths'] * 100, 1)
    new_recov = round(
        comp_country[0]['NewRecovered']/full_stats['Global']['NewRecovered'] * 100, 1)
    total_recov = round(
        comp_country[0]['TotalRecovered']/full_stats['Global']['TotalRecovered'] * 100, 1)

    # Insert comparison statistics into GUI
    stats_display.insert(
        tk.END, f"Percentage of new confirmed cases: {per_new_case}%")
    stats_display.insert(tk.END, "\n")
    stats_display.insert(
        tk.END, f"Percentage of total confirmed cases: {total_con_case}%")
    stats_display.insert(tk.END, "\n")
    stats_display.insert(tk.END, f"Percentage of new death(s): {new_deaths}%")
    stats_display.insert(tk.END, "\n")
    stats_display.insert(
        tk.END, f"Percentage of total death(s): {total_deaths}%")
    stats_display.insert(tk.END, "\n")
    stats_display.insert(tk.END, f"Percentage of new recovered: {new_recov}%")
    stats_display.insert(tk.END, "\n")
    stats_display.insert(
        tk.END, f"Percentage of total recovered: {total_recov}%")

# GUI blocks

# Header Welcome
title = tk.Label(text="Welcome to live country wise statistics of COVID-19.",
                 font=("Helvetica", 20, "bold"))
title.grid(column=0, row=0, ipadx=45)

title1 = tk.Label(text="", font=("Helvetica"))
title1.grid(column=0, row=1)

# Prompt for Global Stats
title2 = tk.Label(text="Click below to get a summary of global statistics", font=(
    "Helvetica", 14, "bold"))
title2.grid(column=0, row=2)

button1 = tk.Button(text="Update", command=summary_display)
button1.grid(column=0, row=3)

title3 = tk.Label(text="", font=("Helvetica"))
title3.grid(column=0, row=5)

# Prompt for Country Stats
title4 = tk.Label(text="Enter name of country below to get statistical update", font=(
    "Helvetica", 14, "bold"))
title4.grid(column=0, row=6)

entry = tk.Entry()
entry.grid(column=0, row=7)

button2 = tk.Button(text="Update", command=country_display)
button2.grid(column=0, row=8)

title5 = tk.Label(text="", font=("Helvetica"))
title5.grid(column=0, row=10)

# Prompt for Country Comparison with Global Stats
title6 = tk.Label(text="Enter name of country below to compare with world statistics", font=(
    "Helvetica", 14, "bold"))
title6.grid(column=0, row=11)

entry2 = tk.Entry()
entry2.grid(column=0, row=12)

button3 = tk.Button(text="Update", command=percent_display)
button3.grid(column=0, row=13)

# Start and run GUI
window.mainloop()
