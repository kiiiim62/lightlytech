# LightlyTechnology

![LightlyTechnology!](/assets/images/Lightly.png "LightlyTechnology")

### Links
- [LightlyTech Twitter](https://x.com/lightlytec)
- [LightlyTech Figma](https://www.figma.com/design/sF4cpXZkiBNWwJZbzwSN0W/Lightly?node-id=5-165&node-type=canvas&t=waYj3GG4OgGEk6wL-0)

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Concept & Vision](#concept--vision)
- [Technical Architecture](#technical-architecture)
- [Product and How It Works](#product-and-how-it-works)
- [Problem Statement](#problem-statement)
- [Solutions & Benefits](#solutions--benefits)
- [Testing & Development](#testing--development)
- [Contributing](#contributing)
- [License](#license)
- [About Us](#about-us)


## **Introduction**
Lightly is an intelligent distribution box designed to give homeowners and businesses full control over their energy usage. By integrating real-time energy monitoring, actionable insights, and smart controls, Lightly empowers users to reduce energy consumption, optimize efficiency, and prevent unauthorized usage. With the integration of decentralized technologies like Solana, users can also earn rewards for optimizing their energy consumption.

## **Usage**
To start using Lightly, users simply install the **Lightly Box** in their distribution panel and connect it to the Lightly web app. From there, users can:
- Monitor their energy consumption in real-time.
- Control electrical devices remotely.
- Earn rewards for energy efficiency through our Solana-based token system.

Users can also use **Solana-based** tokens to gain rewards, engage in decentralized energy trading, or redeem their tokens for smart home products and services.

## **Concept & Vision**
Our vision is to revolutionize energy consumption by making it smarter, more efficient, and decentralized. Lightly not only allows users to monitor and manage their energy consumption but also enables them to be part of a **decentralized energy grid** where they can **earn tokens** for optimizing energy usage and share their energy data with the community.

We believe that empowering users with real-time insights and control will lead to significant reductions in energy waste, lower bills, and a more sustainable energy grid. The integration of **Solana** for token-based rewards and energy trading adds an extra layer of engagement and value for users.

## **Technical Architecture**
Lightly’s architecture is built around the following key components:
1. **ESP32-based hardware**: The Lightly Box is powered by the ESP32 microcontroller, which handles real-time data collection and control.
2. **Mobile/Web App**: The app (built using React Native for mobile) communicates with the ESP32 via Wi-Fi and displays real-time energy data on a chart while allowing users to send control commands.
3. **Blockchain Integration**: We leverage **Solana** for token rewards, decentralized energy trading, and immutable data storage of energy usage records.
4. **MQTT Protocol**: For low-latency communication between the web app and ESP32, we utilize MQTT.



## **Product and How It Works**
![How Lightly Works!](/assets/images/How-it-Works.png "How Lightly Works")
1. **Installation**: The Lightly Box is installed in the distribution panel and connected to the electrical system.
2. **Data Collection**: The ESP32 collects real-time data on energy usage, such as power consumption per appliance.
3. **Monitoring & Control**: The Lightly app displays energy usage data and provides controls to turn off or on specific devices remotely.
4. **Reward System**: Users earn tokens for energy optimization through decentralized rewards powered by Solana, and they can participate in an energy marketplace.
5. **Energy Insights**: The web app provides detailed insights and recommendations based on usage patterns to help users save energy and reduce costs.

## **Problem Statement**
In today’s power distribution systems, consumers face several issues:
- **Lack of real-time monitoring**: Users are unaware of their energy consumption until they receive their monthly bill.
- **Inefficient usage**: Without actionable data, users cannot optimize their energy consumption.
- **Energy theft and unauthorized consumption**: Energy providers and consumers suffer losses due to untracked or unauthorized energy usage.
- **Lack of rewards for energy efficiency**: Consumers have no incentive to optimize their energy usage beyond lowering their bills.

## **Solutions & Benefits**
Lightly addresses these issues by providing:
1. **Real-Time Monitoring**: Track energy usage live via the Lightly app, making it easier to understand consumption patterns.
2. **Energy Control**: Control appliances remotely, giving users the ability to reduce energy waste.
3. **Solana Integration**: Earn tokens through efficient energy usage and decentralized energy trading.
4. **Usage Insights**: Get actionable insights and recommendations for optimizing energy consumption.
5. **Cost Reduction**: Minimize unnecessary energy consumption, resulting in lower energy bills.
6. **Scalability**: Lightly can be deployed in homes, businesses, and even large utility networks.

## **Testing & Development**
To contribute to the development or test the app, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/dayosalam/lightlytech.git
    ```
2. Install dependencies for the web app (React Native):
    ```bash
    cd lightlytech
    npm install
    ```
3. Set up your development environment for ESP32 communication.
4. Start the development server:
    ```bash
    npm start
    ```


Contributions to the web3 features: Coming Soon!!!

## **Contributing**
We welcome contributions from developers, designers, and blockchain enthusiasts. Here's how you can contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit:
    ```bash
    git commit -m "Your message"
    ```
4. Push your changes:
    ```bash
    git push origin feature-branch
    ```
5. Submit a Pull Request (PR), and we’ll review it as soon as possible.

### **Issues**
If you encounter any bugs or have suggestions, feel free to open an issue on GitHub.

## **License**
Lightly is released under the MIT License, making it open-source and freely available for anyone to use, modify, and distribute. See the [LICENSE](./LICENSE) file for more details.

## **About Us**
Lightly was developed by a passionate team dedicated to revolutionizing energy management and creating a sustainable future. With expertise spannng software engineering, embedded systems engineering, and designing, our goal is to empower consumers with the tools and insights they need to optimize their energy usage and reduce their environmental footprint. With Lightly, we're making energy smart, efficient, and rewarding.

If you have any questions or would like to learn more, feel free to reach out via our GitHub discussions or follow us on [Twitter](https://x.com/lightlytec) for updates!



