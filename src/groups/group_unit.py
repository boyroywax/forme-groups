from attrs import define, field, validators

from .merkle_tree import MerkleTree
from .group_subunit import GroupSubUnit
from .nonce import Nonce


@define(frozen=True, slots=True)
class GroupUnit:
    nonce: Nonce = field(validator=validators.instance_of(Nonce))
    owners: GroupSubUnit = field(validator=validators.instance_of(GroupSubUnit))
    creds: GroupSubUnit = field(validator=validators.instance_of(GroupSubUnit))
    data: GroupSubUnit = field(validator=validators.instance_of(GroupSubUnit))

    def __str__(self) -> str:
        output_str: str = ""
        output_str += "Nonce: " + str(self.nonce) + "\n"
        output_str += "Owners: " + str(self.owners) + "\n"
        output_str += "Creds: " + str(self.creds) + "\n"
        output_str += "Data: " + str(self.data) + "\n"

        return output_str[:-1]

    def __repr__(self) -> str:
        return f"GroupUnit(nonce={self.nonce.__repr__()}, owners={self.owners.__repr__()}, creds={self.creds.__repr__()}, data={self.data.__repr__()})"

    def hash_tree(self) -> MerkleTree:
        nonce_hash: str = self.nonce.hash_tree().root()
        owners_hash: str = self.owners.hash_tree().root()
        creds_hash: str = self.creds.hash_tree().root()
        data_hash: str = self.data.hash_tree().root()

        return MerkleTree([nonce_hash, owners_hash, creds_hash, data_hash])