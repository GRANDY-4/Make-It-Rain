using UnityEngine;

namespace MIR.UI
{
    /// <summary>
    /// Manages all UI elements and canvas interactions.
    /// </summary>
    public class UIManager : MonoBehaviour
    {
        private static UIManager instance;

        public static UIManager Instance
        {
            get
            {
                if (instance == null)
                {
                    instance = FindObjectOfType<UIManager>();
                }
                return instance;
            }
        }

        private void Awake()
        {
            if (instance != null && instance != this)
            {
                Destroy(gameObject);
                return;
            }

            instance = this;
        }

        public void ShowMessage(string message)
        {
            Debug.Log($"[UI] {message}");
        }

        public void ShowError(string error)
        {
            Debug.LogError($"[UI Error] {error}");
        }
    }
}
