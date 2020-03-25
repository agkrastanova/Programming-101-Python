from datetime import datetime, timedelta



def validate_conditions(conditions):
    counter = 0

    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be > 24.')

    if counter != 1:
        raise ValueError('Invalid conditions.')



def ensure_conditions(conditions):
   
    for condition in conditions:
        if not condition.get('hours'): 
            condition['hours'] = 0
    return conditions


def group_conditions(conditions):
    condition = []

    for i in range(len(conditions)-1):
        x = conditions[i].get('hours')
        y = conditions[i+1].get('hours')
        condition.append((x,y))


    return condition



def get_current_condition(conditions):
    return conditions[0]



def get_cancellation_fee(condition, price):
    percent = condition[1]
    return price*(percent / 100)



def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    assert start < now

    validate_conditions(conditions)

    ensured_condition = ensure_conditions(conditions)
    grouped_conditions = group_conditions(conditions)

    

    current = get_current_condition(grouped_conditions)

    return get_cancellation_fee(current,price)



def main():
    now = datetime.now()
    booking_start = now - timedelta(hours=10)
    price = 100
    conditions = [
        { 'hours': 24, 'percent': 10 },
        { 'hours': 12, 'percent': 50 },
        { 'hours': 6, 'percent': 80 },
        { 'percent': 100 }
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)



if __name__ == '__main__':
    main()
