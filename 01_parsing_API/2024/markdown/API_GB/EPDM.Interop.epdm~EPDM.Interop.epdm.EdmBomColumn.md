---
title: "EdmBomColumn Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomColumn"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn.html"
---

# EdmBomColumn Structure

Contains information about a single column in a Bill of Materials.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomColumn
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomColumn : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomColumn : public System.ValueType
```

## Examples

struct EdmBomColumn{ integer mlColumnID ; integer mlVariableID ; enum EdmVariableType mlVariableType ; integer mlFlags ; enum EdmBomColumnType meType ; string mbsCaption ; integer mlWidth ; };

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)

[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## See Also

[EdmBomColumn Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
