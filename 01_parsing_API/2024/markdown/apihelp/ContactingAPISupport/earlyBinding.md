---
title: "Early Binding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "apihelp/ContactingAPISupport/earlyBinding.html"
---

# Early Binding

### Early binding

Creating associations between two entities is called binding. For example,
in the Visual Basic line of codeDim
retval As Long, the variable namedretvalis associated, or binded, to the data typeLong.
When binding occurs at compile time, it is called early binding and it
improves the performance of your program, increases type checking, and
assists in detecting errors in your code.

To implement early binding in the SOLIDWORKS software, you must reference
two type libraries:

- SldWorksversionType Library(sldworks.idl)
- SOLIDWORKSversionConstant type library(swconst.idl)

(Substitute the actual SOLIDWORKS version
number forversion.)

These type libraries:

- Provide descriptions of all of the available SOLIDWORKS
  API objects, properties, methods, events, and constants.
- Are automatically referenced when you record a
  SOLIDWORKS macro.

In Visual Basic, early bound SOLIDWORKS object variables are prefixed
bySldWorks, which tells Visual
Basic to look in the SOLIDWORKS type library. For example,Dim
swApp As Objectis early bound when changed toDim
swApp As SldWorks.SldWorks.
