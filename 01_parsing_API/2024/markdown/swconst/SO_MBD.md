---
title: "System Options > MBD"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_MBD.htm"
---

# System Options > MBD

The following MBD settings are not supported in SOLIDWORKS Connected.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Allow editing of Templates for 3DPDF's (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdit3DPDFTemplate) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdit3DPDFTemplate,
< OnFlag >) | Boolean value |  |
