# Public and private boundary

## Public repository purpose

This repository is the inspectable research layer of RIF. Public material may include original source code, formal specifications, synthetic fixtures, openly licensed inputs, methods, tests, issue discussions and non-confidential research documentation.

## Material that must remain private

Do not commit or place in public issues:

- raw or derived human-subject data that could identify a participant;
- protected health information, biometric identifiers or linkable physiological traces;
- consent forms, recruitment records, contact details or compensation records;
- private institutional-review, ethics or partner correspondence;
- unpublished third-party datasets or material supplied under restricted terms;
- API keys, passwords, tokens, private keys, connection strings or credentials;
- production infrastructure, confidential partner configurations or security-sensitive deployment details.

## Publication test

Before committing a new artifact, establish all of the following:

1. The contributor has the right to publish it.
2. It contains no secret, personal, confidential or restricted information.
3. Any example is synthetic, properly anonymised under an approved process, or lawfully public.
4. Claims are limited to what the code, data and cited evidence establish.
5. A private workspace is used when any condition is not satisfied.

Removing a file from the current branch does not remove it from Git history. Suspected disclosure requires immediate containment, credential rotation where applicable and a separate history-remediation decision.
