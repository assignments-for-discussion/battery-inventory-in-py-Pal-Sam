
def count_batteries_by_health(present_capacities):
  soh_values=[] #list to store soh%
  battery_class=[] #list to store the battery classifications corresponding to soh%

  for i in present_capacities:
    soh_percent=100*(i/120)
    soh_values.append(soh_percent)

  #print(soh_values)

  battery_class_count={  #dictionary to store the number of batteries under healthy, exchange and failed classification
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }

  for i in soh_values:
    if i >80 and i<=100:
      battery_class.append("healthy")
      battery_class_count["healthy"]+=1
    elif i<=80 and i>=62:
      battery_class.append("exchange")
      battery_class_count["exchange"]+=1
    elif i<62:
      battery_class.append("failed")
      battery_class_count["failed"]+=1

  #print(battery_class)
  #print(battery_class_count)
  
  return  battery_class_count


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
