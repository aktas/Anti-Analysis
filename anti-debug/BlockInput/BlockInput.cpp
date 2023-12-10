#include <iostream>
#include <windows.h>

using namespace std;

bool IsHooked()
{
    BOOL bFirstResult = FALSE, bSecondResult = FALSE;
    __try
    {
        bFirstResult = BlockInput(TRUE);
        bSecondResult = BlockInput(TRUE);
    }
    __finally
    {
        BlockInput(FALSE);
    }
    return bFirstResult && bSecondResult;
}

int main()
{
    if (IsHooked()) {
        cout << "Detect Debugger!" << endl;
    } // BlockInput fonksiyonu, kullanıcının giriş aygıtlarını (klavye ve fare) geçici olarak devre dışı bırakma veya etkinleştirme yeteneğine sahiptir. 
    // Kod, bu fonksiyonu iki kez çağırarak hata ayıklama aracının bu fonksiyonu engelleyip engellemediğini kontrol etmeye çalışıyor. 
    // Normalde, bir hata ayıklama aracı bu tür işlemleri engelleyemez, bu nedenle eğer fonksiyon çağrıları başarılıysa, hata ayıklama aracı var gibi düşünülebilir.
}
