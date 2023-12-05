import matplotlib.pyplot as plt

def look_algorithm(initial_position, requests):
    total_head_movement = 0
    order_served = []

    # Sort the requests in ascending order
    sorted_requests = sorted(requests)

    # Find the index where initial_position is in the sorted_requests
    initial_position_index = sorted_requests.index(initial_position)

    # Head movement towards higher track numbers
    for i in range(initial_position_index, len(sorted_requests)):
        order_served.append(sorted_requests[i])
        total_head_movement += abs(sorted_requests[i] - initial_position)
        initial_position = sorted_requests[i]

    # Head movement towards lower track numbers
    for i in range(initial_position_index - 1, -1, -1):
        order_served.append(sorted_requests[i])
        total_head_movement += abs(sorted_requests[i] - initial_position)
        initial_position = sorted_requests[i]

    return total_head_movement, order_served

def plot_graph(order_served):
    plt.plot(range(len(order_served)), order_served, marker='o')
    plt.title('LOOK Disk Scheduling Algorithm')
    plt.xlabel('Order Served')
    plt.ylabel('Track Number')
    plt.show()

if __name__ == "__main__":
    # Input initial position and track requests
    initial_position = int(input("Enter initial position of disk arm: "))
    requests_str = input("Enter track requests separated by spaces: ")
    requests = list(map(int, requests_str.split()))

    # Run LOOK algorithm
    total_head_movement, order_served = look_algorithm(initial_position, requests)

    # Display results
    print(f"Total Head Movement: {total_head_movement}")
    print(f"Order Served: {order_served}")

    # Plot the graph
    plot_graph(order_served)
