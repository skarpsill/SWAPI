---
title: "EdmBomVersion Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomVersion"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion.html"
---

# EdmBomVersion Structure

Contains information about a Bill of Materials version, revision, or label.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomVersion
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomVersion : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomVersion : public System.ValueType
```

## Examples

struct EdmBomVersion{ enum EdmBomVersionType meType ; integer mlVersion ; datetime moDate ; string mbsTag ; string mbsComment ; };

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)

[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## See Also

[EdmBomVersion Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
