def calculate_energy(power, hours):
    """
    Calculate daily energy consumption.
    Energy = Power(W) × Hours / 1000
    """
    return (power * hours) / 1000


def get_recommendation(name, power, hours, energy):
    """
    Rule-based AI recommendation.
    """

    if hours > 10:
        return f"Reduce the daily usage time of {name}."

    elif power > 1500:
        return f"{name} is a high-power appliance. Use it carefully."

    elif energy > 5:
        return f"{name} consumes high energy. Try to reduce its usage."

    elif energy > 2:
        return f"Monitor the usage of {name}."

    else:
        return f"{name} usage is efficient."


def optimize_energy(appliances):
    """
    Analyze all appliances and generate recommendations.
    """

    total_energy = 0
    results = []

    for appliance in appliances:

        name = appliance["name"]
        power = appliance["power"]
        hours = appliance["hours"]

        energy = calculate_energy(power, hours)

        recommendation = get_recommendation(
            name, power, hours, energy
        )

        total_energy += energy

        results.append({
            "name": name,
            "power": power,
            "hours": hours,
            "energy": energy,
            "recommendation": recommendation
        })

    monthly_energy = total_energy * 30

    return results, total_energy, monthly_energy