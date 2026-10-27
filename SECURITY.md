# Security policy

## Supported scope

RIF is an early research prototype, not a hosted service or medical device. Security review presently covers only the source and synthetic demonstrations in this repository.

## Sensitive material

Never commit credentials, private keys, participant data, protected health information, consent records, restricted datasets or private infrastructure configuration. Use synthetic fixtures in bug reports and tests. See [PUBLIC_PRIVATE_BOUNDARY.md](PUBLIC_PRIVATE_BOUNDARY.md).

## Reporting

Report a suspected vulnerability or disclosure privately to the repository owner through an established private contact route. Include the affected revision, expected behaviour, observed behaviour and a minimal reproduction that contains no real participant or credential data. Do not publish an exploit against a live system or any sensitive information in an issue.

There is currently no public bug bounty or separate security-contact address. Acknowledgement of a report does not create a payment entitlement.
