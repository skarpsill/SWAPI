---
title: "Early and Late Binding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Early_and_Late_Binding.htm"
---

# Early and Late Binding

Variable declarations fall into two categories of binding:

- Early binding occurs when an object assigned to
  a variable is declared to be of a specific object type.
- Late binding occurs when an object assigned to
  a variable is declared to be of typeObject.

Early binding improves the performance of your program, increases type
checking, and assists in detecting errors in your code.

To implement early binding in the SOLIDWORKS software, you must[reference two type libraries](../Overview/Type_Libraries.htm):

- SldWorksversionType Library(sldworks.tlb)
- SOLIDWORKSversionConstant type library(**swconst.tlb**)

(Substitute the actual SOLIDWORKS version
number forversion.)

These type libraries:

- Provide descriptions of all of the available SOLIDWORKS
  API objects, properties, methods, events, and constants.
- Are automatically referenced when you record a
  SOLIDWORKS macro.

To early bind SOLIDWORKS object variables, prefix the variable's object type withSldWorks.,
which tells Visual Basic to look in the SldWorks type library.

For example:

(Table)=========================================================

| Change late binding... | To early binding... |
| --- | --- |
| Dim swApp As Object | Dim swApp As SldWorks.SldWorks |
| Dim swModel As Object | Dim swModel As SldWorks.ModelDoc2 |
| Dim swEntity As Object | Dim swEntity As SldWorks.Entity |
