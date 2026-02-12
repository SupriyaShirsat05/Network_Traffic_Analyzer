import pandas as pd

normal = pd.read_csv("Documents/CN ML Project/CSV Files/normal_tcp_big.csv")
attack = pd.read_csv("Documents/CN ML Project/CSV Files/syn_flood.csv")

#Droping rows where IP is missing 
normal = normal.dropna(subset=["ip.src", "ip.dst"])
attack = attack.dropna(subset=["ip.src", "ip.dst"])

normal["label"] = 0
attack["label"] = 1

print("Normal packets:", len(normal))
print("Attack packets:", len(attack))

attack_balanced = attack.sample(
	n=len(normal),
	random_state=42
)
	
balanced_df = pd.concat([normal, attack_balanced])
balanced_df = balanced_df.sample(frac=1, random_state=42)

balanced_df.to_csv("balanced_tcp_dataset.csv", index = False)

print("Final balanced dataset size:", len(balanced_df))
print(balanced_df["label"].value_counts())


