---
title: "SldWorks::GetDocumentDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetDocumentDependencies.htm"
---

# SldWorks::GetDocumentDependencies

T his
method is obsolete and has been superseded by[SldWorks::GetDocumentDependencies2](sldworksAPI.chm::/SldWorks/SldWorks__GetDocumentDependencies2.htm).

Description

This method gets all the model dependencies for a document. The document
does not have to be open.

Syntax (OLE Automation)

retval = SldWorks.GetDocumentDependencies(
docName, traverseflag, SearchFlag)

(Table)=========================================================

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest
level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies,
FALSE to look where the documents were last saved |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; there are two strings for each
document returned in this list of dependent files; the first is the file
name and the second is the filename with the complete pathname; this combination
repeats itself for each dependent file found for this ModelDoc2 |

Syntax
(COM)

status = SldWorks->IGetDocumentDependencies(docName,
traverseflag, SearchFlag, &retval)

(Table)=========================================================

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest
level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies,
FALSE to look where the documents were last saved |
| Output: | (BSTR) retval | Array of strings; there are two strings for each document returned in
this list of dependent files; the first is the file name and the second
is the filename with the complete pathname; this combination repeats itself
for each dependent file found for this ModelDoc2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

As an example, calling this method on a drawing document returns a list
of all the part, assemblies, or both, used in the drawing. If you set
the traverseFlag to TRUE, then each of the parts within the assembly file
are also returned in this array of strings.

Another example would be calling this method with a derived mirror part.
Because a derived mirror part is generated from another part, the list
of model dependencies returned by this method would include the original
the part used to generate the derived mirror part.

Library features are unassociated. They do not require the library nor
do they update when changes are made to the Library feature. Therefore,
this method does not return Library features.

For the COM implementation, see SldWorks::GetDocumentDependenciesCount
to determine the number of strings to be returned.

If you use this method with an assembly that contains two documents,Part1and SubAssem1, an example
of what might be returned is:

["Part1",
"C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM"]

IftraverseFlagisset to TRUE, then all
the documents contained in SubAssem1.ASM would also be returned. Suppressed
components are still recognized and returned by this method as a dependent
file.

NOTE:If the SearchFlag is set to TRUE, then the current directory is set to
the directory of the docName file. This replicates the interactive behavior
of theReferencesbutton in the
File Open dialog window.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\SldWorks\SldWorks__GetDocumentDependencies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DocumentDependencies_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\SldWorks\SldWorks__GetDocumentDependencies.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
