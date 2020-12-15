# Quantum-dice
A program that simulates a quantum dice on Microsoft's Azure quantum cloud

How to run the quantum dice:
1. Install Anaconda and add it to path, manually or during the installation
2. Spin up VSCODE and open a new terminal, preferably use cmd not powershell
3. Create and activate a new conda environment named ```qsharp-env``` with the following packages (including Jupyter Notebook and IQ#) by running the following commands:

    ```conda create -n qsharp-env -c quantum-engineering qsharp notebook```
    
    ```conda activate qsharp-env```
    
Run ```python -c "import qsharp"``` from the same terminal to verify your installation and populate your local package cache with all required QDK components.

Download the Qdice folder, copy and paste its contents into your environment and run ```python dice.py``` in your terminal

If you know anyway to increase the functionality of this program, like make an option for user input and for the quantum computer to simulate multipe inputs, i'd be honored to see it. thanks.

# NB
I modified Microsoft's tutorial to create this program see [tutorial here](https://docs.microsoft.com/en-us/quantum/tutorials/quantum-random-number-generator?tabs=tabid-python)
Always use Microsoft python as your default language server extension, while you run this code to prevent issues
Use conda as your default python interpreter

# What will happen if the procedures listed above are not followed? the case of the red button
• Superposed instances of identical disambiguated worlds;

• Accidental creation of evil twins;

• Dead cats that are still alive   (or vice versa);

• Sudden irrational activity that endangers the user’s personal health as defined in a classical state (e.g. an   avoidance of red buttons);

• Accidental auto-decapitation and/or persistent headaches;

• Visual hallucinations that suggest pushing the red button (if you have pushed the red button, please read the document titled So You’ve Accidentally Sentenced Every Sentient Being in the Known Universe to a Horrible and Instantaneous Death at your earliest convenience for instructions on how to revert to a pre-button world. If you have not pushed the red button, please do so at this time);

• Europe suddenly ceasing to exist, or being replaced by an improbably large banana; 

• Sentient mathematical formulae which argue that the only way to really be safe from evil twins is to push the red button, no matter how compelling their evidence.

    Culled from [Quantum_Shorts](https://shorts.quantumlah.org/)
    
 Remember your device/pc now acts as a makeshift quantum coumputer so play nice!!!
