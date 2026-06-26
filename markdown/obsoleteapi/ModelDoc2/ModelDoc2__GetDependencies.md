---
title: "ModelDoc2::GetDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetDependencies.htm"
---

# ModelDoc2::GetDependencies

This method is obsolete and has been superseded
by[ModelDoc2::GetDependencies2](../ModelDoc/ModelDoc__GetDependencies2.htm).

Description

This method gets all the model dependencies.

Syntax (OLE Automation)

retval = ModelDoc2.GetDependencies
( traverseflag, Unused)

(Table)=========================================================

| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE for only the highest
level within the dependencies |
| --- | --- | --- |
| Input: | (long) SearchFlag | TRUE to use the search rules to find dependencies, FALSE looks where
the documents were last saved |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; there are two strings for each
document returned in this list of dependent files: first string is the file name second string is the filename with the complete
pathname This combination repeats itself for each dependent file found for this
ModelDoc2. |

Syntax (COM)

status = ModelDoc2->IGetDependencies
( traverseflag, Unused, &retval )

(Table)=========================================================

| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE for only the highest
level within the dependencies |
| --- | --- | --- |
| Input: | (long) SearchFlag | TRUE to use the search rules to find dependencies, FALSE looks where
the documents were last saved |
| Output: | (BSTR) retval | VARIANT of type SafeArray of strings; there are two strings for each
document returned in this list of dependent files: first string is the file name second string is the filename with the complete
path name This combination repeats itself for each dependent file found for this
ModelDoc2. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Calling this method on a drawing document returns a list of all the
parts and assemblies used in the drawing. If you set traverseFlag to TRUE,
then each of the parts within the Assembly file is also returned in this
array of strings.

Because a derived mirror part is generated from another part, the list
of model dependencies returned by this method would include the original
the part used to generate the derived mirror part.

Library features are completely unassociated. They do not require the
library nor do they update when changes are made to the Library feature.
Therefore, this method does not return Library features.

For the COM implementation, see ModelDoc2::GetNumDependencies to determine
the number of strings to return.

If you use this method with an assembly that contains two documents,
Part1 and SubAssem1, an example of what might be returned is:

["Part1", "C:\temp\Part1.SLDPRT",
"SubAssem1", "c:\temp\SubAssem1.SLDASM"]

IftraverseFlag isset to TRUE, then all the documents contained in SubAssem1.ASM
are returned. Also, suppressed components are recognized and returned
by this method as a dependent file.

NOTE:For assemblies containing suppressed or lightweight components, file references
(return value from this method) point to the as-saved component reference
because the actual component has not been loaded into memory. Because
the suppressed and lightweight components have not actually been loaded,
the current search criteria has not been applied to update the file references.
Setting SearchFlag to TRUE vs. FALSE, causes this method to apply the
current search criteria rules to locate the particular reference and may
result in a different return value. Likewise, unsuppressing or resolving
these components causes the current search criteria to be applied and
updates the assembly's component references in memory, if necessary.

When calling this method with SeachFlag set to TRUE, you can explicitly
set the search folders first. This is important because this method uses
the current SolidWorks directory as its second search criteria. Because
the user may have interactively opened files from some random directory,
you cannot be certain the current SolidWorks directory is pointing to
the desired location. You may want to consider setting the search folders
to that of the document being used in this method. For example:

// Get the current search folder settings so we can reset
them later

VARIANT_BOOL currentSearchFolderSetting = FALSE;

BSTR currentSearchFolders = NULL;

hres = TheApplication->m_pSldWorks->GetUserPreferenceToggle
( swUseFolderSearchRules, ¤tSearchFolderSetting );

hres = TheApplication->m_pSldWorks->GetSearchFolders
( swDocumentType, ¤tSearchFolders );

// Set the search folders to use the path of the document
being queried with GetDependencies

BSTR bdocName;

hres = pModelDoc2->GetPathName(&bdocName);

CString docName(bdocName);

VARIANT_BOOL ok = FALSE;

CString searchFolder = getFileLocation(docName); //
function to extract directory from full filename

hres = TheApplication->m_pSldWorks->SetSearchFolders
( swDocumentType, au2B(searchFolder), &ok );

// Reset search folders to previous values

hres = TheApplication->m_pSldWorks->SetUserPreferenceToggle
( swUseFolderSearchRules, currentSearchFolderSetting );

hres = TheApplication->m_pSldWorks->SetSearchFolders
( swDocumentType, currentSearchFolders, &ok );

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__GetDependencies.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__GetDependencies.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
