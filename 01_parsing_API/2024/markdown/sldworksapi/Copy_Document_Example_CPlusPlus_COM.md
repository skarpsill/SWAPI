---
title: "Copy Document Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_Example_CPlusPlus_COM.htm"
---

# Copy Document Example (C++ COM)

This example shows how to copy documents.

// -------------------------------------------------------------------

void APITestFunction()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= VARIANT_FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetVal
= -1;

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CComPtr <ISldWorks> kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pSldWorks;
```

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s1,
s2, s3[1], s4[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}error
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s1
= SysAllocString(_T("c:\\temp\\1\\assem1.sldasm"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s2
= SysAllocString(_T("c:\\temp\\2\\2\\assem2.sldasm"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s3[0]
= SysAllocString(_T("c:\\temp\\1\\part1.sldprt"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s4[0]
= SysAllocString(_T("c:\\temp\\2\\2\\part2.sldprt"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
connect to SW

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->ICopyDocument(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s1,
s2,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}s3,
s4,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMoveCopyOptionsOverwriteExistingDocs
+ swMoveCopyOptionsCreateNewFolder,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}&error);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

} //void APITestFunction()

// -------------------------------------------------------------------
