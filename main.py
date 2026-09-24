from multiweb_assistant.pipeline import ask, build_multiweb_assistant


def main():

    try:
        print("Building the multiweb assistant...")

        agent = build_multiweb_assistant()

        if agent is None:
            print("Error: Could not build the multiweb assistant.")
            return

        print("Assistant ready!\n")

        demo_questions = [
            "Tell me something about machine learning project?",
            "Tell me something about his experences?"
        ]

        for question in demo_questions:

            try:
                print("=" * 70)
                print("QUESTION:", question)
                print("-" * 70)

                answer = ask(agent, question)

                print("ANSWER:", answer)
                print("=" * 70)
                print()

            except Exception as e:
                print(f"Error processing question '{question}': {e}")

    except Exception as e:
        print(f"Error starting the multiweb assistant: {e}")


if __name__ == "__main__":
    main()