from multiweb_assistant.pipeline import ask, build_multiweb_assistant
def main():
    print("Building the multiweb assistant...")
    agent = build_multiweb_assistant()
    print("Assistant ready!\n")
    
    demo_questions = [
        "Tell me something about machine learning project?",
        "Tell me something about his experences?"
    ]
    
    for question in demo_questions:
        print("="*70)
        print("QUESTION:",question)
        print("-"*70)
        answer = ask(agent,question)
        print("ANSWER:",answer)
        print("="*70)
        print()

if __name__=="__main__":
    main()