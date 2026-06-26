---
title: "PostMessageToApplication Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PostMessageToApplication"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.html"
---

# PostMessageToApplication Method (ISldWorks)

Posts a message to the application that invoked this method.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PostMessageToApplication( _
   ByVal Cookie As System.Integer, _
   ByVal UserData As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim UserData As System.Integer

instance.PostMessageToApplication(Cookie, UserData)
```

### C#

```csharp
void PostMessageToApplication(
   System.int Cookie,
   System.int UserData
)
```

### C++/CLI

```cpp
void PostMessageToApplication(
   System.int Cookie,
   System.int UserData
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Cookie`: Cookie specified in

[ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `UserData`: Additional message-specific information defined by the application

## VBA Syntax

See

[SldWorks::PostMessageToApplication](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PostMessageToApplication.html)

.

## Examples

Contact SOLIDWORKS API Support to obtain either the 32-bit or 64-bit version of**C++ 32-bit and 64-bit Add-ins Post Messages After Every Selection**.

## Remarks

If your application must be x64 compatible, then use

[ISldWorks::PostMessageToApplicationx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~PostMessageToApplicationx64.html)

.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
