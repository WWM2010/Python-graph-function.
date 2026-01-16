import matplotlib.pyplot as plt
import numpy as np

def run_math_lab_pdf():
    print("=== Math Function to PDF Saver ===")
    print("Enter a mathematical function of x (e.g., 'np.sin(x)', 'x**2', 'np.exp(-x**2) * np.cos(2 * np.pi * x)'):")
    
    while True:
        func_str = input("\nEnter function f(x) (or 'exit'): ").strip()
        if func_str.lower() == 'exit': break
            
        try:
            # Using 2000 points for extra smoothness in the PDF
            x = np.linspace(-10, 10, 2000)
            
            # Use np.pi so the user can just type 'pi' in their string
            y = eval(func_str, {"np": np, "x": x, "pi": np.pi})

            plt.figure(figsize=(10, 6))
            plt.plot(x, y, color='blue', label=f"y = {func_str}")
            
            # Focus the view (prevents tangent functions from going to infinity)
            plt.ylim(-15, 15) 
            
            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            plt.grid(True, linestyle=':', alpha=0.6)
            plt.title(f"Graph of {func_str}")
            plt.legend()

            # --- THE SAVING PART ---
            filename = input("Enter filename to save (e.g., 'my_graph'): ")
            if not filename.endswith('.pdf'):
                filename += ".pdf"
            
            plt.savefig(filename, format='pdf')
            print(f"Successfully saved to {filename}")
            
            plt.show() # Still shows the graph on screen

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_math_lab_pdf()