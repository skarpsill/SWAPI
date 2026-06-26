---
title: "Write Parasolid Partition Stream to File Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm"
---

# Write Parasolid Partition Stream to File Example (C++)

This example shows how to write a Parasolid partition stream to a file
using the SOLIDWORKS Document Manager API.

#import 'C:\Program Files\Common Files\SOLIDWORKS Shared\swdocumentmgr.dll'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}raw_interfaces_only,
raw_native_types, no_namespace, named_guids //Change as necessary

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

wchar_t* filename = "87-part.sldprt"

wchar_t* outputDir = "c:\\caddocs\\";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

ISwDMClassFactoryPtr swClassFact;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swClassFact.CreateInstance(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}__uuidof(SwDMClassFactory)
);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(ISwDMClassFactory*)swClassFact)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISwDMApplicationPtr
swDocMgr(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swClassFact->GetApplication("your_license_key")
); //Specify your license
key

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(ISwDMApplication*)swDocMgr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SwDmDocumentOpenError
error;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISwDMDocumentPtr
swDoc( swDocMgr->GetDocument(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}filename,
swDmDocumentPart, TRUE, &error ) );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(ISwDMDocument*)swDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISwDMConfigurationMgrPtr
swCfgMgr(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDoc->ConfigurationManager);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(ISwDMConfigurationMgr*)swCfgMgr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_variant_t
names( swCfgMgr->GetConfigurationNames()
);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SAFEARRAY*
nameArray = names.parray;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(int i=0; i<nameArray->rgsabound[0].cElements; ++i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_bstr_t
str( ((BSTR*)(nameArray->pvData))[i] );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISwDMConfigurationPtr
swCfg(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCfgMgr->GetConfigurationByName(str) );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISwDMConfiguration2*
pswCfg2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(swCfg)

swCfg->QueryInterface( __uuidof(ISwDMConfiguration2),
(void **)&pswCfg2 );

else

return 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
dir( outputDir );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dir
+= "\\";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dir
+= str;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dir
+= ".xmp_bin";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pswCfg2->GetPartitionStream( (LPCTSTR)dir );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
