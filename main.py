from random import randint
from icebreaker import Icebreaker
from runner import Runner


if __name__ == "__main__":
    armitage = Runner("armitage", max_integrity=50, power=randint(1, 20), finesse=randint(1, 20))
    molly = Runner("molly", max_integrity=50, power=randint(1, 20), finesse=randint(1, 20))

    if armitage.get_power() > armitage.get_finesse():
        armitage_icebreaker = Icebreaker("Pipeline", 8, 13, "fracter")
    else:
        armitage_icebreaker = Icebreaker("Pipeline", 8, 13, "decoder")

    if molly.get_power() > molly.get_finesse():
        molly_icebreaker = Icebreaker("Pipeline", 8, 13, "fracter")
    else:
        molly_icebreaker = Icebreaker("Pipeline", 8, 13, "decoder")

    armitage.equip(armitage_icebreaker)
    molly.equip(molly_icebreaker)

    print("=== NETRUN DUEL ===\n")
    print(f"{armitage.get_handle()}: Power={armitage.get_power()}, Finesse={armitage.get_finesse()}")
    print(f"{molly.get_handle()}: Power={molly.get_power()}, Finesse={molly.get_finesse()}")
    print(f"{armitage.get_handle()} ha equipaggiato {armitage_icebreaker.get_name()}")
    print(f"{molly.get_handle()} ha equipaggiato {molly_icebreaker.get_name()}")

    print("\n=== INIZIO COMBATTIMENTO ===\n")

    turno = 1
    combattenti = [armitage, molly]

    while True:
        print(f"--- Turno {turno} ---")

        attaccante = combattenti[(turno + 1) % 2]
        bersaglio = combattenti[turno % 2]

        danno = attaccante.attack(bersaglio)
        print(f"{attaccante.get_handle()} attacca {bersaglio.get_handle()} e infligge {danno} danni")
        print(bersaglio)

        if not bersaglio.is_alive():
            break

        turno += 1
        print()

    print("\n=== FINE COMBATTIMENTO ===\n")

    if armitage.is_alive() and not molly.is_alive():
        print(f"{armitage.get_handle()} vince!")
    elif molly.is_alive() and not armitage.is_alive():
        print(f"{molly.get_handle()} vince!")
    else:
        print("Pareggio!")